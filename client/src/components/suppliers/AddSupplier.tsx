import { Box, Button, Stack, TextField } from "@mui/material";
import * as React from "react";
import { useCallback, useState } from "react";
import { postSupplier } from "../../api/supplier";
import { regexEmail, regexLetters, regexPhone } from "../../api/constants";

export interface IAddBranchResponse {
  id: string;
  name: string;
  city: string;
  employees: any[];
  stocks: any[];
}

const convertToObject = (json: any): IAddBranchResponse => {
  return {
    id: json._id,
    name: json.name,
    city: json.city,
    employees: [],
    stocks: []
  };
};

export const AddSupplier = () => {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");

  const doRequest = useCallback((nameReq: string, phoneReq: string, emailReq: string) => {
    postSupplier(nameReq, phoneReq, emailReq)
      .then( async (response) => {
        if (response.ok) alert(`Supplier "${nameReq}" was successfully added!`);
        else {
          const result = await response.text();
          alert(JSON.parse(result).message);
        }
      })
      .catch((e) => alert(`Error occurred: ${e.message}`));
  }, [convertToObject, postSupplier]);


  const [helperTextPhone, setHelperTextPhone] = useState("");
  const [helperTextEmail, setHelperTextEmail] = useState("");

  return (
    <Box style={{ width: "60%" }}>
      <Stack spacing={2}>
        <h2> Add new supplier </h2>
        <TextField
          style={{ width: "80%" }}
          label="Name"
          variant="standard"
          required
          onChange={(e) => setName(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Phone"
          placeholder="+79997775566"
          variant="standard"
          required
          type="phone"
          helperText={helperTextPhone}
          onChange={(e) => {
            if (regexPhone.test(e.target.value)) {
              setPhone(e.target.value);
              setHelperTextPhone("");
            }
            else {
              setHelperTextPhone("Phone format should be: +79998887766");
            }
          }}
        />
        <TextField
          style={{ width: "80%" }}
          label="Email"
          helperText={helperTextEmail}
          placeholder="supplier@gmail.com"
          variant="standard"
          required
          type="email"
          onChange={(e) => {
            if (regexEmail.test(e.target.value)) {
              setEmail(e.target.value);
              setHelperTextPhone("");
            }
            else {
              setHelperTextEmail("Email format should be: supplier@gmail.com");
            }
        }}
        />
        <Box style={{ marginLeft: "35%" }} flexDirection="row">
          <Button
            disabled={!name.length || !phone.length
              || !regexPhone.test(phone) || !email.length || !regexEmail.test(email)}
            onClick={() => doRequest(name, phone, email)}
          >
            ADD
          </Button>

        </Box>
      </Stack>
    </Box>
  );
};
