import * as React from "react";
import {useState} from "react";
import {Box, Tab, Tabs, Typography} from "@mui/material";
import {SalesList} from "./SalesList";
import {AddSale} from "./AddSale";
import {TabPanel} from "components/tabs/tabs";

export const Sales = () => {
  const [isOpenForm, setOpenForm] = useState(false);
  const [tabValue, setTabValue] = useState(0);
  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <Typography component="div" variant="h3"> Sales page </Typography>
      <Box flexDirection={"row"}>
        <Tabs value={tabValue} onChange={handleChange}>
          <Tab
            label="List sales"
          />
          <Tab
            label="Add new sale"
          />
        </Tabs>
      </Box>
      <TabPanel value={tabValue} index={0}>
        <SalesList />
      </TabPanel>
      <TabPanel value={tabValue} index={1}>
        <AddSale />
      </TabPanel>
    </Box>
  );
};
