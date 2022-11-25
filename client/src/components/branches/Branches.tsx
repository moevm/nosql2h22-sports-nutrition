import * as React from "react";
import { Box, IconButton, Tab } from "@mui/material";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import { Link as RouterLink } from "react-router-dom";
import { BranchesList } from "./BranchesList";

export const Branches = () => {
  return (
    <Box>
      <Box flexDirection={"row"} >
      <h1> Branches page </h1>
        <Tab
          sx={{display: "flex", marginRight: 0, alignSelf: "end"}}
          component={RouterLink}
          to="/branches/add"
          value="add"
          label={
            <label key="label" title="Add new branch">
              Add new branch
              <IconButton color="inherit" aria-label="Add new branch">
                <AddCircleOutlineIcon />
              </IconButton>
            </label>
          }
        />
      </Box>
      <BranchesList />
    </Box>
  );
};
