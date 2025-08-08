SELECT 
    employee_id, 
    department, 
    age, 
    benefit_type, 
    enrollment_date, 
    usage_date 
FROM 
    employee_benefits
WHERE 
    enrollment_date >= '2022-01-01';
