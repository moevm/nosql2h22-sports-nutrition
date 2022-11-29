import { HOST, SERVER_PORT } from "../constants";
import { GetBranchDto, objToQueryString } from "./functions";
import { modeAndHeaders } from "./constants";

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

export const getBranch = (res: GetBranchDto): Promise<Response> => {
  return fetch(`${HOST}${SERVER_PORT}/branch?${objToQueryString(res)}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const getFilteredStocks = (branchId: string, filter: FilterStocksCriteria) => {
  const query = objToQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/stock?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};