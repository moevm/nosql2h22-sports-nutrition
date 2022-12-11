import {toQueryString} from "./functions";
import {HOST, SERVER_PORT} from "../constants";
import {modeAndHeaders} from "./constants";

export interface FilterEmployeesCriteria {
  _id?: string;
  role?: string;
  phone_number?: string;
  name?: string;
  employment_date_from?: string;
  employment_date_to?: string;
  salary_from?: string;
  salary_to?: string;
  surname?: string;
  patronymic?: string;
  dismissal_date_from?: string;
  dismissal_date_to?: string;
}
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

export const findEmployeesInBranch = (filter: FilterEmployeesCriteria, branchId?: string) => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/employee?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const findEmployee = (filter: FilterEmployeesCriteria) => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/employee?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const getEmployeeById = (id: string) => {
  return fetch(`${HOST}${SERVER_PORT}/employee?_id=${id}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const postEmployee = (id: string, employeeData: EmployeeData) => {
  console.log("Body: ", JSON.stringify(employeeData));
  return fetch(`${HOST}${SERVER_PORT}/branch/${id}/employee`,
    {
      method: "POST",
      ...modeAndHeaders,
      body: JSON.stringify(employeeData)
    });
};
