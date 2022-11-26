export const getSupplier = (id: string): Promise<Response> => {
  return fetch(`http://localhost:8008/supplier/${id}`, {
    method: "GET",
    mode: "cors",
    headers: { "Content-Type": "application/json", Accept: "application/json" }
  });
};