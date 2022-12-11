import {HOST, SERVER_PORT} from "../constants";
import {toQueryString} from "./functions";
import {modeAndHeaders} from "./constants";

export interface FilterStocksCriteria {
  _id?: string;
  supplier_id?: string;
  product_id?: string;
  name?: string;
  amount_from?: string;
  amount_to?: string;
  price_from?: string;
  price_to?: string;
}

export interface FilterBranchCriteria {
  _id?: string;
  city?: string;
  name?: string;
  product_names?: string;
  stocks_to?: string;
  stocks_from?: string;
  employees_to?: string;
  employees_from?: string;
  employee_names?: string;
  employee_surnames?: string;
  employee_ids?: string;
  product_ids?: string;
}

export const isObjEmpty = (filter: any) => {
  return Object.values(filter).every(el => el === undefined);
};

export const postBranch = (nameReq: string, cityReq: string) => {
  return fetch(`${HOST}${SERVER_PORT}/branch`, {
    method: "POST",
    ...modeAndHeaders,
    body: JSON.stringify({ name: nameReq, city: cityReq })
  });
};

export const postStock = (branchId: string, productId: string, price: number,
                          amount: number) => {
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/stock`, {
    method: "POST",
    ...modeAndHeaders,
    body: JSON.stringify({ product_id: productId, price, amount })
  });
};

export const getBranchesPage = (pageSize: number, currentPage: number) => {
  return fetch(`${HOST}${SERVER_PORT}/branch/page?size=${pageSize}&page=${currentPage}`, {
    method: "GET",
    ...modeAndHeaders
  });
};

export const getFilteredBranches = (filter: FilterBranchCriteria): Promise<Response> => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/branch?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const getFilteredStocks = (branchId: string, filter: FilterStocksCriteria) => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/stock?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const importBranches = (obj: any) => {
  return fetch(`${HOST}${SERVER_PORT}/maintenance/branch`, {
    method: "POST",
    ...modeAndHeaders,
    body: obj
  });
};