import { HOST, SERVER_PORT } from "../constants";
import { GetBranchDto, objToQueryString } from "./functions";

export const postBranch = (nameReq: string, cityReq: string) => {
  return fetch(`${HOST}${SERVER_PORT}/branch`, {
    method: "POST",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ name: nameReq, city: cityReq })
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
  console.log("PATH: ", `${HOST}${SERVER_PORT}/branch?${objToQueryString(res)}`);
  return fetch(`${HOST}${SERVER_PORT}/branch?${objToQueryString(res)}`,
    {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" }
    });
};