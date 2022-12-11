import * as React from "react";
import { useState } from "react";
import { Box, Tab, Tabs, Typography } from "@mui/material";
import { SuppliersList } from "./SuppliersList";
import { FindSupplier } from "./FindSupplier";
import { AddSupplier } from "./AddSupplier";
import { TabPanel } from "components/tabs/tabs";
import { FindProductsEverywhere } from "../products/FindProductsEverywhere";

export const Suppliers = () => {
  const [tabValue, setTabValue] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <Typography component="div" variant="h3"> Suppliers page </Typography>
      <Box flexDirection={"row"}>
        <Tabs value={tabValue} onChange={handleChange}>
          <Tab
            label="Suppliers list"
          />
          <Tab
            label="Add new supplier"
          />
          <Tab
            label="Find supplier"
          />
          <Tab
            label="Find product"
          />
        </Tabs>
      </Box>
      <TabPanel value={tabValue} index={0}>
        <SuppliersList />
      </TabPanel>
      <TabPanel value={tabValue} index={1}>
        <AddSupplier />
      </TabPanel>
      <TabPanel value={tabValue} index={2}>
        <FindSupplier />
      </TabPanel>
      <TabPanel value={tabValue} index={3}>
        <FindProductsEverywhere />
      </TabPanel>
    </Box>
  );
};
