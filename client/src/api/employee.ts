import { objToQueryString } from "./functions";
import { HOST, SERVER_PORT } from "../constants";
import { FilterEmployeesCriteria } from "./branch";

export const getFilteredEmployees = (filter: FilterEmployeesCriteria, branchId?: string) => {
  const query = objToQueryString(filter);
  console.log("PATH: ", `${HOST}${SERVER_PORT}/branch/${branchId}/employee?${query}`);
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/employee?${query}`,
    {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" }
    });
};

export const findEmployee = (id: string) => {
  return fetch(`${HOST}${SERVER_PORT}/employee/${id}`,
    {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" }
    });
};