import * as React from 'react';
import { Box, IconButton, Tab, Tabs } from '@mui/material';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import { Link as RouterLink } from "react-router-dom";

export const Branches = () => {
  return (
    <Box>
      <h1> Branches page </h1>
      <Tabs>
        <Tab
          component={RouterLink}
          to="/branches/add"
          value="add"
          label={
            <label key="label" title="Add new branch">
              <IconButton color="inherit" aria-label="Add new branch">
                <AddCircleOutlineIcon />
              </IconButton>
            </label>
          }
        />
      </Tabs>
    </Box>
  );
};
