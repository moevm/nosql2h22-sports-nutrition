import * as React from "react";
import {Box, Tab} from "@mui/material";
import {Link as RouterLink} from "react-router-dom";

export const Main = () => {
  return <Box>
    <h2> Welcome to Sport nutrition information system! </h2>
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
      value="sales"
      label="Sales"
      component={RouterLink}
      to="/sales"
    />
  </Box>;
};
