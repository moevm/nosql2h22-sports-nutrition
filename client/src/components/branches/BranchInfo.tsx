import { Stack, TextField } from "@mui/material";
import * as React from "react";

export const BranchInfo = ({ branch }: { branch: any }) => {
  return (
    <Stack spacing={2}>
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