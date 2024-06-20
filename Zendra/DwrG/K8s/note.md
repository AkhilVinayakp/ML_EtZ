APPs
1. Strapi
    dependency: postgress.
    

2. postgress.
    uses claim: p-hp-cl0


3.volumn
    id: p-hp-vl0 name: hpdata
    claim: p-hp-cl0



4.airflow



# commands
- kubectl apply -f hp_vlm.yaml    
creates a volumn

- kubectl apply -f hp_clm.yaml
deploy the claims


