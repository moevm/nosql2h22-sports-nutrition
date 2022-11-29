import { Box, IconButton, Stack, TextField } from "@mui/material";
import * as React from "react";
import { useCallback, useState } from "react";
import CancelIcon from "@mui/icons-material/Cancel";
import AddIcon from "@mui/icons-material/Add";
import { useNavigate } from "react-router-dom";
import { postSupplier } from "../../api/supplier";

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
          variant="standard"
          required
          type="phone"
          onChange={(e) => setPhone(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Email"
          variant="standard"
          required
          type="email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <Box style={{ marginLeft: "35%" }} flexDirection="row">
          <IconButton
            title="Add new supplier"
            component="span"
            onClick={() => doRequest(name, phone, email)}
          >
            <AddIcon />
          </IconButton>

          <IconButton component="span" title="Cancel" onClick={() => navigate("/suppliers")}>
            <CancelIcon />
          </IconButton>
        </Box>
      </Stack>
    </Box>
  );
};
