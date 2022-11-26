import { Params } from "react-router-dom";

export function objToQueryString(obj: any) {
  const keyValuePairs = [];
  console.log("OBJ: ", obj);
  for (const key in obj) {
    console.log("key: ", key, obj[key]);
    if (obj[key] && obj[key] !== " ") {
      keyValuePairs.push(encodeURIComponent(key) + "=" + encodeURIComponent(obj[key]));
    }
  }
  return keyValuePairs.join("&");
}

export interface GetBranchDto {
  name?: string;
  _id?: string;
  city?: string;
}

export const makeBranchDtoFromParams = (params: Readonly<Params<string>>): GetBranchDto => {
  console.log("params: ", params);
  return {
    name: params.name,
    city: params.city,
    _id: params._id
  };
};

export const makeBranchDtoFromStrings = (name: string, city: string, id: string): GetBranchDto => {
  return {
    name: name.length ? name : undefined,
    city: city.length ? city : undefined,
    _id: id.length ? id : undefined
  };
};