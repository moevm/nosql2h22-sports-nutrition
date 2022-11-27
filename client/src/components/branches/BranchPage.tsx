import { NotFound } from "../NotFound";
import { Box, Tab, Tabs } from "@mui/material";
import * as React from "react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getBranch } from "../../api/branch";
import { makeBranchDtoFromParams } from "../../api/functions";
import { TabPanel } from "../tabs";
import { BranchInfo } from "./BranchInfo";


export const BranchPage = () => {
  const params = useParams();

  useEffect(() => {
    getBranch(makeBranchDtoFromParams(params))
      .then((response) => response.json())
      .then((json) => {
        setBranch(json.result[0]);
      });
  }, [params]);


  const [branch, setBranch] = useState<any>(undefined);
  const [tabValue, setTabValue] = useState(0);

  if (!branch) {
    return <NotFound />;
  }

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <h2> Branch {branch.name} </h2>
      <Box flexDirection={"row"}>
        <Tabs value={tabValue} onChange={handleChange}>
          <Tab
            label="Info"
          />
          <Tab
            label="Employees"
          />
          <Tab
            label="Stocks"
          />
        </Tabs>
      </Box>
      <TabPanel value={tabValue} index={0}>
        <BranchInfo branch={branch}/>
      </TabPanel>
      <TabPanel value={tabValue} index={1}>
      </TabPanel>
      <TabPanel value={tabValue} index={2}>
      </TabPanel>
    </Box>
  );
};
