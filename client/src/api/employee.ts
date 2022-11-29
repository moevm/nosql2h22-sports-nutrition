import { objToQueryString } from "./functions";
import { HOST, SERVER_PORT } from "../constants";
import { FilterEmployeesCriteria } from "./branch";
import { modeAndHeaders } from "./constants";

export interface EmployeeData {
  name: string,
  surname: string,
  patronymic: string,
  passport: string,
  phone: string,
  city: string,
  employment_date: string,
  salary: number,
  role: string
}

export const getFilteredEmployees = (filter: FilterEmployeesCriteria, branchId?: string) => {
  const query = objToQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/employee?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const findEmployee = (id: string) => {
  return fetch(`${HOST}${SERVER_PORT}/employee/${id}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const postEmployee = (id: string, employeeData: EmployeeData) => {
  return fetch(`${HOST}${SERVER_PORT}/branch/${id}/employee`,
    {
      method: "POST",
      ...modeAndHeaders,
      body: JSON.stringify(employeeData)
    });
};
