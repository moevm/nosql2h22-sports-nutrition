import { Box, IconButton, Stack, TextField } from "@mui/material";
import * as React from 'react';
import CancelIcon from '@mui/icons-material/Cancel';
import AddIcon from '@mui/icons-material/Add';
import { useNavigate } from 'react-router-dom';
import { useCallback, useState } from 'react';

export interface IAddBranchResponse {
  id: string;
  name: string;
  city: string;
  employees: any[];
  stocks: any[];
}

const convertToObject = (json: any): IAddBranchResponse => {
  return {
    id: json._id,
    name: json.name,
    city: json.city,
    employees: [],
    stocks: []
  };
};

export const AddBranch = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<IAddBranchResponse>();
  const [name, setName] = useState('');
  const [city, setCity] = useState('');

  const doRequest = useCallback((nameReq: string, cityReq: string) => {
    console.log('Do request: ', nameReq, cityReq);
    fetch(`http://localhost:8080/branch`, {
      method: 'POST',
      mode: 'cors',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ name: nameReq, city: cityReq }),
    })
      .then((response) => response.json())
      .then((json) => {
        const parsedJson = convertToObject(json);
        setData(parsedJson);
      });
  }, []);
  return (
    <Box style={{width: "60%"}}>
      <Stack spacing={2}>
      <h2> Add new branch </h2>
      <TextField
        style={{width: "80%"}}
        id="outlined-basic"
        label="Name"
        variant="outlined"
        required
        onChange={(e) => setName(e.target.value)}
      />
      <TextField
        style={{width: "80%"}}
        id="filled-basic"
        label="City"
        variant="outlined"
        required
        onChange={(e) => setCity(e.target.value)}
      />
        <Box style={{marginLeft: "35%"}} flexDirection="row">
      <IconButton title="Add new branch" component="span" onClick={() => doRequest(name, city)}>
        <AddIcon />
      </IconButton>
      <IconButton
          component="span" title="Cancel" onClick={() => navigate('/branches')}>
        <CancelIcon />
      </IconButton>
        </Box>
      </Stack>
    </Box>
  );
};
