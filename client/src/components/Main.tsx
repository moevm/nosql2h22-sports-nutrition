import * as React from "react";
import { useState } from "react";
import { Box, Tab, Tabs, Typography } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";

export const Main = () => {
  return <Box>
    <Typography component="div" variant={"h3"}> Welcome to Sport nutrition information system! </Typography>
    <Tabs indicatorColor="secondary" textColor="inherit">
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
