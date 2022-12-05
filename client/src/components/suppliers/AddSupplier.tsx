import { Box, Button, IconButton, Stack, TextField } from "@mui/material";
import * as React from "react";
import { useCallback, useState } from "react";
import { useNavigate } from "react-router-dom";
import { postSupplier } from "../../api/supplier";
import { regexPhone, regexEmail } from "../../api/constants";

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
  const navigate = useNavigate();
  const [data, setData] = useState<IAddBranchResponse>();
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");

  const doRequest = useCallback((nameReq: string, phoneReq: string, emailReq: string) => {
    postSupplier(nameReq, phoneReq, emailReq)
      .then((response) => response.json())
      .then((json) => {
        const parsedJson = convertToObject(json);
        setData(parsedJson);
        navigate("/suppliers");
      });
  }, [convertToObject, postSupplier]);
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
          onChange={(e) => setPhone(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Email"
          placeholder="supplier@gmail.com"
          variant="standard"
          required
          type="email"
          onChange={(e) => setEmail(e.target.value)}
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
