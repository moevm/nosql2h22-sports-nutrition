FROM mongo:6.0.2

ARG DATABASE_URI

ENV DATABASE_URI ${DATABASE_URI}

COPY suppliers.json /suppliers.json
COPY branches.json /branches.json

CMD mongoimport --uri ${DATABASE_URI} --collection suppliers --type json --file /suppliers.json --jsonArray && \
    mongoimport --uri ${DATABASE_URI} --collection branches --type json --file /branches.json --jsonArray
