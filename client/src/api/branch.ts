import { HOST, SERVER_PORT } from "../constants";
import { GetBranchDto, objToQueryString } from "./functions";

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

export const isFilterEmpty = (filter: FilterStocksCriteria) => {
  return  Object.values(filter).every(el => el === undefined);
}

export const postBranch = (nameReq: string, cityReq: string) => {
  return fetch(`${HOST}${SERVER_PORT}/branch`, {
    method: "POST",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ name: nameReq, city: cityReq })
  });
};

export const postStock = (branchId: string, productId: string, price: number,
                          amount: number) => {
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/stock`, {
    method: "POST",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ product_id: productId, price, amount })
  });
};

export const getBranchesPage = (pageSize: number, currentPage: number) => {
  return fetch(`${HOST}${SERVER_PORT}/branch/page?size=${pageSize}&page=${currentPage}`, {
    method: "GET",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" }
  });
};

export const getBranch = (res: GetBranchDto): Promise<Response> => {
  return fetch(`${HOST}${SERVER_PORT}/branch?${objToQueryString(res)}`,
    {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" }
    });
};

export const getFilteredStocks = (branchId: string, filter: FilterStocksCriteria) => {
  const query = objToQueryString(filter);
  console.log("PATH: ", `${HOST}${SERVER_PORT}/branch/${branchId}/stock?${query}`);
  return fetch(`${HOST}${SERVER_PORT}/branch/${branchId}/stock?${query}`,
    {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" }
    });
};