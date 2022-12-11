import { toQueryString } from "./functions";
import { HOST, SERVER_PORT } from "../constants";
import { modeAndHeaders } from "./constants";

export interface FilterProductCriteria {
  _id?: string;
  names?: string;
  descriptor_ids?: string;
  price_to?: string;
  price_from?: string;
  supplier_ids?: string;
}

export const getProducts = (filter: FilterProductCriteria) => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/product?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const getProductsOfSupplier = (filter: FilterProductCriteria, supplierId: string) => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/supplier/${supplierId}/product?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};