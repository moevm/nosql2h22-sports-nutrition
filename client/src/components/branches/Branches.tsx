import * as React from "react";
import { useState } from "react";
import { Box, Tab, Tabs, Typography } from "@mui/material";
import { BranchesList } from "./BranchesList";
import { FindBranch } from "./FindBranch";
import { AddBranch } from "./AddBranch";
import { TabPanel } from "components/tabs/tabs";
import { EmployeeInAllBranches } from "../employees/EmployeesInAllBranches";

export const Branches = () => {
  const [isOpenForm, setOpenForm] = useState(false);
  const [tabValue, setTabValue] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <Typography component="div" variant="h3"> Branches page </Typography>
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
          <Tab
            label="Find employee"
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
        <FindBranch setOpen={setOpenForm} />
      </TabPanel>
      <TabPanel value={tabValue} index={3}>
        <EmployeeInAllBranches />
      </TabPanel>
    </Box>
  );
};
