import {HOST, SERVER_PORT} from "../constants";
import {toQueryString} from "./functions";
import {modeAndHeaders} from "./constants";

export const postSale = (branchIdReq: string, productIdReq: string, supplierIdReq: string, priceReq: string, amountReq: string) => {
    return fetch(`${HOST}${SERVER_PORT}/sale`, {
      method: "POST",
      ...modeAndHeaders,
      body: JSON.stringify({ branch_id: branchIdReq, product_id: productIdReq, supplier_id: supplierIdReq, price: priceReq, amount: amountReq })
    });
  };