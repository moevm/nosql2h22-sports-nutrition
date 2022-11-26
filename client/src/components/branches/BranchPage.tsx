import { NotFound } from "../NotFound";
import { Stack, TextField } from "@mui/material";
import * as React from "react";


export const BranchPage = ({ branch }: { branch: any }) => {
  if (!branch) {
    return <NotFound />;
  }
  return (
    <Stack spacing={2}>
      <h2> Branch {branch.name} </h2>
      <TextField
        style={{ width: "80%" }}
        id="outlined-basic"
        label="Id"
        variant="outlined"
        InputProps={{
          readOnly: true
        }}
        value={branch._id}
      />
      <TextField
        style={{ width: "80%" }}
        id="outlined-basic"
        label="Name"
        variant="outlined"
        InputProps={{
          readOnly: true
        }}
        value={branch.name}
      />
      <TextField
        style={{ width: "80%" }}
        id="filled-basic"
        label="City"
        variant="outlined"
        InputProps={{
          readOnly: true
        }}
        value={branch.city}
      />
    </Stack>
  );
};
