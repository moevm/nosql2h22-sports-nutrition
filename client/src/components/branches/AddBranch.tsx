import {Box, Button, Stack, TextField} from "@mui/material";
import * as React from "react";
import {useCallback, useState} from "react";
import {useNavigate} from "react-router-dom";
import {postBranch} from "../../api/branch";
import {checkOnError} from "../../api/functions";

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

export const AddBranch = () => {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [city, setCity] = useState("");

  const doRequest = useCallback((nameReq: string, cityReq: string) => {
    postBranch(nameReq, cityReq)
      .then((response) =>
          checkOnError(response, "Branch was successfully added!"))
      .catch((e) => alert(`Error occurred: ${e.message}`));
  }, [postBranch, convertToObject]);


  return (
    <Box style={{ width: "60%" }}>
      <Stack spacing={2}>
        <h2> Add new branch </h2>
        <TextField
          style={{ width: "80%" }}
          label="Name"
          variant="standard"
          required
          onChange={(e) => setName(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="City"
          variant="standard"
          required
          onChange={(e) => setCity(e.target.value)}
        />
        <Box style={{ marginLeft: "35%" }} flexDirection="row">
          <Button onClick={() => doRequest(name, city)}
                  disabled={!name.length || !city.length}>
            Add
          </Button>
          <Button onClick={() => navigate("/branches")}>
            Cancel
          </Button>
        </Box>
      </Stack>
    </Box>
  );
};
