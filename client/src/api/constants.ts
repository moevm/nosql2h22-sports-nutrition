export const modeAndHeaders: RequestInit = {
  mode: "cors",
  headers: { "Content-Type": "application/json", "Accept": "application/json",
    "Access-Control-Allow-Origin" : "*"}
};

const makeRangeSentence = (from: string, to: string) => {
  return `${from} must be less than or equal to ${to}`
}
export const priceRange = makeRangeSentence("Price from", "price to")

export const stocksRange = makeRangeSentence("Stocks from", "stocks to")

export const employeesRange = makeRangeSentence("Employee from", "employee to")
export const amountRange = makeRangeSentence("Amount from", "amount to")
export const salaryRange = makeRangeSentence("Salary from", "salary to")
export const regexLetters = /^[A-Za-zА-Яа-я]*$/;
export const regexPhone = /^(\+)[1-9][0-9\-\(\)\.]{9,15}$/;
export const regexEmail = /([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+/;