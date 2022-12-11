import {Stack, TextField} from "@mui/material";
import * as React from "react";

export const BranchInfo = ({ branch }: { branch: any }) => {
  return (
    <Stack spacing={2}>
      <TextField
        style={{ width: "80%" }}
        label="Id"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={branch._id}
      />
      <TextField
        style={{ width: "80%" }}
        label="Name"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={branch.name}
      />
      <TextField
        style={{ width: "80%" }}
        label="City"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={branch.city}
      />
    </Stack>
  );
};