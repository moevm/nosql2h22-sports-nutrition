import { NotFound } from "../NotFound";
import { Box, IconButton, Tab, Tabs } from "@mui/material";
import * as React from "react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getBranch } from "../../api/branch";
import { makeBranchDtoFromParams } from "../../api/functions";
import { TabPanel } from "../tabs";
import { BranchInfo } from "./BranchInfo";
import { StocksList } from "../stocks/StocksList";
import { AddStockToBranch } from "../stocks/AddStockToBranch";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import SearchOutlinedIcon from '@mui/icons-material/SearchOutlined';
import { EmployeesList } from "../employees/EmployeesList";

export const BranchPage = () => {
  const params = useParams();

  const [branch, setBranch] = useState<any>(undefined);
  const [tabValue, setTabValue] = useState(0);
  const [isOpenForm, setOpenForm] = useState(false);
  const [stocks, setStocks] = useState<any[]>([]);

  useEffect(() => {
    getBranch(makeBranchDtoFromParams(params))
      .then((response) => response.json())
      .then((json) => {
        setBranch(json.result[0]);
        setStocks(json.result[0].stocks);
      });
  }, [params, getBranch, makeBranchDtoFromParams]);


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
        <BranchInfo branch={branch} />
      </TabPanel>
      <TabPanel value={tabValue} index={1}>
        <EmployeesList employees={branch.employees} />
      </TabPanel>
      <TabPanel value={tabValue} index={2}>
        <Box flexDirection="row" >
        <IconButton color="inherit" title="Add new stock"
                    style={{ width: "2em", margin: "10px" }}
                    onClick={() => setOpenForm(!isOpenForm)}>
          <AddCircleOutlineIcon />
        </IconButton>
          <IconButton color="inherit" title="Filter stocks"
                      style={{ width: "2em", margin: "10px" }}>
            <SearchOutlinedIcon />
          </IconButton>
        </Box>
        <AddStockToBranch isOpen={isOpenForm} setOpen={setOpenForm} branchId={branch._id}
                          stocks={stocks} setStocks={setStocks} />
        <StocksList stocks={stocks} />
      </TabPanel>
    </Box>
  );
};
