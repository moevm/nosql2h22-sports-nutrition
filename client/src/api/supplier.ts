import {HOST, SERVER_PORT} from "../constants";
import {modeAndHeaders} from "./constants";
import {toQueryString} from "./functions";

export interface FilterSupplierCriteria {
  _id?: string;
  phone?: string;
  name?: string;
  email?: string;
  employment_date_to?: string;
  product_names?: string;
  product_ids?: string;
  descriptor_ids?: string;
}

export const getSupplierById = (id: string): Promise<Response> => {
  return fetch(`${HOST}${SERVER_PORT}/supplier?_id=${id}`, {
    method: "GET",
    ...modeAndHeaders
  });
};

export const getSupplier = (filter: FilterSupplierCriteria) => {
  const query = toQueryString(filter);
  return fetch(`${HOST}${SERVER_PORT}/supplier?${query}`,
    {
      method: "GET",
      ...modeAndHeaders
    });
};

export const postSupplier = (nameReq: string, phoneReq: string, emailReq: string) => {
  return fetch(`${HOST}${SERVER_PORT}/supplier`, {
    method: "POST",
    ...modeAndHeaders,
    body: JSON.stringify({ name: nameReq, phone: phoneReq, email: emailReq })
  });
};

export const getSupplierPage = (pageSize: number, currentPage: number, productsSize: number = 5) => {
  return fetch(`${HOST}${SERVER_PORT}/supplier/page?size=${pageSize}&page=${currentPage}&products_size=${productsSize}`, {
    method: "GET",
    ...modeAndHeaders
  });
};

export const postProduct = (id: string, name: string, price: number) => {
  return fetch(`${HOST}${SERVER_PORT}/supplier/${id}/product`, {
    method: "POST",
    ...modeAndHeaders,
    body: JSON.stringify({ price, descriptor: { name } })
  });
};

export const importSuppliers = (obj: any) => {
  return fetch(`${HOST}${SERVER_PORT}/maintenance/supplier`, {
    method: "POST",
    ...modeAndHeaders,
    body: obj
  });
};