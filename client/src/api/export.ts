import {HOST, SERVER_PORT} from "../constants";
import {modeAndHeaders} from "./constants";

export const exportBranchesPage = (pageSize: number, currentPage: number) => {
  return fetch(`${HOST}${SERVER_PORT}/maintenance/branch/page?size=${pageSize}&page=${currentPage}`, {
    method: "GET",
    ...modeAndHeaders
  });
};

export const exportSuppliersPage = (pageSize: number, currentPage: number) => {
  return fetch(`${HOST}${SERVER_PORT}/maintenance/supplier/page?size=${pageSize}&page=${currentPage}`, {
    method: "GET",
    ...modeAndHeaders
  });
};