import { NotFound } from "../NotFound";
import { Box, IconButton, Tab, Tabs, Typography } from "@mui/material";
import * as React from "react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { FilterEmployeesCriteria, getBranch, getFilteredStocks, isObjEmpty } from "../../api/branch";
import { makeBranchDtoFromParams } from "../../api/functions";
import { TabPanel } from "components/tabs/tabs";
import { BranchInfo } from "./BranchInfo";
import { StocksList } from "../stocks/StocksList";
import { AddStockToBranch } from "../stocks/AddStockToBranch";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import { EmployeesList } from "../employees/EmployeesList";
import { FindStockDialog } from "../stocks/FindStockDialog";
import { FilterStocksCriteria } from "api/branch";
import { FindEmployeesDialog } from "../employees/FindEmployeesDialog";
import { getFilteredEmployees } from "../../api/employee";
import { AddEmployee } from "../employees/AddEmployee";

export const BranchPage = () => {
  const params = useParams();

  const [branch, setBranch] = useState<any>(undefined);
  const [tabValue, setTabValue] = useState(0);
  const [isOpenForm, setOpenForm] = useState(false);
  const [isOpenEmployeeForm, setOpenEmployeeForm] = useState(false);
  const [stocks, setStocks] = useState<any[]>([]);
  const [employees, setEmployees] = useState<any[]>([]);
  const [stockFilterCriteria, setStockFilterCriteria] = useState<FilterStocksCriteria>({});
  const [employeeFilterCriteria, setEmployeeFilterCriteria] = useState<FilterEmployeesCriteria>({});

  useEffect(() => {
    getBranch(makeBranchDtoFromParams(params))
      .then((response) => response.json())
      .then((json) => {
        setBranch(json.result[0]);
        setStocks(json.result[0].stocks);
        setEmployees(json.result[0].employees);
      });
  }, [params, getBranch, makeBranchDtoFromParams]);

  useEffect(() => {
    if (!branch || isObjEmpty(stockFilterCriteria)) {
      return;
    }
    getFilteredStocks(branch._id, stockFilterCriteria)
      .then((response) => response.json())
      .then((json) => {
        setStocks(json.result);
      });
  }, [stockFilterCriteria]);

  useEffect(() => {
    if (!branch || isObjEmpty(employeeFilterCriteria)) {
      return;
    }
    getFilteredEmployees(employeeFilterCriteria, branch._id)
      .then((response) => response.json())
      .then((json) => {
        setEmployees(json.result);
      });
  }, [employeeFilterCriteria]);

  if (!branch) {
    return <NotFound />;
  }

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <Typography variant="h4"> Branch {branch.name} </Typography>
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
        <IconButton color="inherit" title="Add new employee"
                    style={{ width: "2em", margin: "10px" }}
                    onClick={() => setOpenEmployeeForm(!isOpenEmployeeForm)}>
          <AddCircleOutlineIcon />
        </IconButton>
        <AddEmployee isOpen={isOpenEmployeeForm} setOpen={setOpenEmployeeForm} branchId={branch._id}
                     employees={employees}
                     setEmployees={setEmployees} />
        <FindEmployeesDialog onChange={setEmployeeFilterCriteria}
                             value={employeeFilterCriteria} />
        <EmployeesList employees={employees} />
      </TabPanel>

      <TabPanel value={tabValue} index={2}>
        <Box flexDirection="row">
          <IconButton color="inherit" title="Add new stock"
                      style={{ width: "2em", margin: "10px" }}
                      onClick={() => setOpenForm(!isOpenForm)}>
            <AddCircleOutlineIcon />
          </IconButton>
        </Box>
        <AddStockToBranch isOpen={isOpenForm} setOpen={setOpenForm} branchId={branch._id}
                          stocks={stocks} setStocks={setStocks} />
        <FindStockDialog onChange={setStockFilterCriteria}
                         value={stockFilterCriteria} />
        <StocksList stocks={stocks} />
      </TabPanel>
    </Box>
  );
};
