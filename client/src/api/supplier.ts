import { HOST, SERVER_PORT } from "../constants";

export const getSupplier = (id: string): Promise<Response> => {
  return fetch(`${HOST}${SERVER_PORT}/supplier/${id}`, {
    method: "GET",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" }
  });
};

export const postSupplier = (nameReq: string, phoneReq: string, emailReq: string) => {
  return fetch(`${HOST}${SERVER_PORT}/supplier`, {
    method: "POST",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ name: nameReq, phone: phoneReq, email: emailReq })
  });
};

export const getSupplierPage = (pageSize: number, currentPage: number) => {
  return fetch(`${HOST}${SERVER_PORT}/supplier/page?size=${pageSize}&page=${currentPage}`, {
    method: "GET",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" }
  });
};