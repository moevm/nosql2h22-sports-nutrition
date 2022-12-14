import {NotFound} from "../NotFound";
import {Box, Button, Tab, Tabs, Typography} from "@mui/material";
import * as React from "react";
import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import {getFilteredBranches, getFilteredStocks, isObjEmpty} from "../../api/branch";
import {branchDtoFromParams, checkOnError} from "../../api/functions";
import {TabPanel} from "components/tabs/tabs";
import {BranchInfo} from "./BranchInfo";
import {StocksList} from "../stocks/StocksList";
import {AddStockToBranch} from "../stocks/AddStockToBranch";
import {EmployeesList} from "../employees/EmployeesList";
import {FindStockDialog} from "../stocks/FindStockDialog";
import {FilterStocksCriteria} from "api/branch";
import {EmployeesDialog} from "../employees/EmployeesDialog";
import {FilterEmployeesCriteria, findEmployeesInBranch} from "../../api/employee";
import {AddEmployee} from "../employees/AddEmployee";

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
    getFilteredBranches(branchDtoFromParams(params))
      .then((response) => response.json())
      .then((json) => {
        setBranch(json.result[0]);
        setStocks(json.result[0].stocks);
        setEmployees(json.result[0].employees);
      });
  }, [params, getFilteredBranches, branchDtoFromParams]);

  useEffect(() => {
    if (!branch || isObjEmpty(stockFilterCriteria)) {
      return;
    }

    getFilteredStocks(branch._id, stockFilterCriteria)
      .then((response) => checkOnError(response))
      .then((json) => {
        if (json) {
          setStocks(json.result);
        }
      })
      .catch((err) => alert(err.message));
  }, [stockFilterCriteria, getFilteredStocks]);

  useEffect(() => {
    if (!branch || isObjEmpty(employeeFilterCriteria)) {
      return;
    }
    findEmployeesInBranch(employeeFilterCriteria, branch._id)
      .then((response) => checkOnError(response))
      .then((json) => {
          if (json) {
              setEmployees(json.result);
          }
      })
      .catch((err) => alert(err.message));
  }, [employeeFilterCriteria, findEmployeesInBranch]);

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
        <Button onClick={() => setOpenEmployeeForm(!isOpenEmployeeForm)}>
          Add new employee
        </Button>
        <AddEmployee isOpen={isOpenEmployeeForm} setOpen={setOpenEmployeeForm} branchId={branch._id}
                     employees={employees}
                     setEmployees={setEmployees} />
        <EmployeesDialog onChange={setEmployeeFilterCriteria}
                         value={employeeFilterCriteria} />
        <EmployeesList employees={employees} />
      </TabPanel>

      <TabPanel value={tabValue} index={2}>
        <Box flexDirection="row">
          <Button onClick={() => setOpenForm(!isOpenForm)}>
            Add new stock
          </Button>
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
