import { HOST, SERVER_PORT } from "../constants";
import { modeAndHeaders } from "./constants";

export const getSupplier = (id: string): Promise<Response> => {
  return fetch(`${HOST}${SERVER_PORT}/supplier/${id}`, {
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

export const getSupplierPage = (pageSize: number, currentPage: number) => {
  return fetch(`${HOST}${SERVER_PORT}/supplier/page?size=${pageSize}&page=${currentPage}`, {
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