% Compute Term-by-term Percentages of Cases with Concurrences
% Written By: Patrick C. Wohlfarth and Andrew D. Martin
% Date: 4/14/2011
% 
% Note: the basic approach here could be used to compute the
% fraction of cases in each term that has any number of
% judge-specific attributes.  This currently works with the 
% citation as the unit of analysis; it could be re-run on 
% any unit of anaysis. 
% 
% load data and create variable for any concurrence
use SCDB_2011_01_justiceCentered_Citation.dta
gen concurrences = 0
replace concurrences = 1 if vote == 3
replace concurrences = 1 if vote == 4

% compute the number of concurrences for each caseId
collapse (sum) concurrences, by(caseId term)
gen concurDummy = 0
replace concurDummy = 1 if concurrences > 0
drop concurrences

% collapse down to the term
sort term
by term: gen cases = _n
collapse (sum) concurDummy (count) cases, by(term)
rename concurDummy concurCount
gen concurPercent = (concurCount/cases) * 100

% save resulting data file
save "concurrences.dta", replace