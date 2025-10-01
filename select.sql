SELECT distinct
subject_id
, insurance
, language
, marital_status
, race
, b.*
FROM main.hosp_admissions as a
left join main.hosp_patients as b
    using (subject_id)
where subject_id = 10000032