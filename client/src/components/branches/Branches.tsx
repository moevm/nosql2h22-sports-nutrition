import * as React from "react";
import { useState } from "react";
import { Box, IconButton, Tab, Tabs, Typography } from "@mui/material";
import { BranchesList } from "./BranchesList";
import { FindBranchDialog } from "./FindBranchDialog";
import { AddBranch } from "./AddBranch";
import { TabPanel } from "components/tabs/tabs";

export const Branches = () => {
  const [isOpenForm, setOpenForm] = useState(false);
  const [tabValue, setTabValue] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <h1> Branches page </h1>
      <Box flexDirection={"row"}>
        <Tabs value={tabValue} onChange={handleChange}>
          <Tab
            label="Branches list"
          />
          <Tab
            label="Add new branch"
          />
          <Tab
            label="Find branches"
            onClick={() => setOpenForm(!isOpenForm)}
          />
        </Tabs>
      </Box>
      <TabPanel value={tabValue} index={0}>
        <BranchesList />
      </TabPanel>
      <TabPanel value={tabValue} index={1}>
       <AddBranch />
      </TabPanel>
      <TabPanel value={tabValue} index={2}>
        <FindBranchDialog isOpen={isOpenForm} setOpen={setOpenForm} />
      </TabPanel>
    </Box>
  );
};
