import * as React from "react";
import { Box, Tab, Tabs } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";
import { useState } from "react";

export const Main = () => {
  const [value, setValue] = useState(undefined);
  return <Box>
    <h1> Welcome to Sport nutrition information system! </h1>
    <Tabs value={value} indicatorColor="secondary" textColor="inherit">
      <Tab
        component={RouterLink}
        to="/branches"
        value="branches"
        label="Branches"
      />
      <Tab
        value="suppliers"
        label="Suppliers"
        component={RouterLink}
        to="/suppliers"
      />
      <Tab
        value="Sales"
        label="Sales"
        component={RouterLink}
        to="/sales"
      />
    </Tabs>
  </Box>;
};
