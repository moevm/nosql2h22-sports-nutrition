import { Box, IconButton, Stack, TextField } from '@mui/material';
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
    stocks: [],
  };
};

export const AddSupplier = () => {
  const navigate = useNavigate();
  const [data, setData] = useState<IAddBranchResponse>();
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  const doRequest = useCallback((nameReq: string, phoneReq: string, emailReq: string) => {
    fetch('http://localhost:8080/supplier', {
      method: 'POST',
      mode: 'cors',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ name: nameReq, phone: phoneReq, email: emailReq }),
    })
      .then((response) => response.json())
      .then((json) => {
        const parsedJson = convertToObject(json);
        setData(parsedJson);
        navigate('/suppliers');
      });
  }, [convertToObject]);
  return (
    <Box style={{ width: '60%' }}>
      <Stack spacing={2}>
        <h2> Add new supplier </h2>
        <TextField
          style={{ width: '80%' }}
          id="outlined-basic"
          label="Name"
          variant="outlined"
          required
          onChange={(e) => setName(e.target.value)}
        />
        <TextField
          style={{ width: '80%' }}
          id="filled-basic"
          label="Phone"
          variant="outlined"
          required
          type="phone"
          onChange={(e) => setPhone(e.target.value)}
        />
        <TextField
          style={{ width: '80%' }}
          id="filled-basic"
          label="Email"
          variant="outlined"
          required
          type="email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <Box style={{ marginLeft: '35%' }} flexDirection="row">
          <IconButton
            title="Add new supplier"
            component="span"
            onClick={() => doRequest(name, phone, email)}
          >
            <AddIcon />
          </IconButton>

          <IconButton component="span" title="Cancel" onClick={() => navigate('/suppliers')}>
            <CancelIcon />
          </IconButton>
        </Box>
      </Stack>
    </Box>
  );
};
