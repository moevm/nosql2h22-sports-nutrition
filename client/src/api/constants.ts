export const modeAndHeaders: RequestInit = {
  mode: "cors",
  headers: { "Content-Type": "application/json", Accept: "application/json" }
};

export const regexPhone = /^(\+)[1-9][0-9\-\(\)\.]{9,15}$/
export const regexEmail= /([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+/