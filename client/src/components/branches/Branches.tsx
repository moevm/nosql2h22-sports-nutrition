import * as React from "react";
import { useState } from "react";
import { Box, IconButton, Tab, Tabs } from "@mui/material";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import { Link as RouterLink } from "react-router-dom";
import { BranchesList } from "./BranchesList";
import { FindBranchDialog } from "./FindBranchDialog";

export const Branches = () => {
  const [isOpenForm, setOpenForm] = useState(false);
  return (
    <Box>
      <Box flexDirection={"row"}>
        <h1> Branches page </h1>
        <Tabs>
          <Tab
            sx={{ display: "flex", marginRight: 0, alignSelf: "end" }}
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
          <Tab
            value="find"
            label="Find branches"
            onClick={() => setOpenForm(!isOpenForm)}
          />
        </Tabs>
      </Box>
      <FindBranchDialog isOpen={isOpenForm} setOpen={setOpenForm} />
      <BranchesList />
    </Box>
  );
};
