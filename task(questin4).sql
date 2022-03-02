Create Table Task (
	country					varchar2(100),
	tdate						date,
	daily_vaccinations	Number(10),
	vaccines					varchar2(100)
);
/
-- import data 
/
Declare
	V_MEDIAN	Number;
Begin
	For REC In (
		Select 
				*
			From Task
			Order By daily_vaccinations
	) Loop
		V_MEDIAN := 0;
		Begin
			Select MEDIAN(daily_vaccinations) OVER (PARTITION BY country) 
					Into V_MEDIAN
				From Task 
					Where country = REC.country 
						And tdate = REC.tdate
						And vaccines = REC.vaccines;

			Update Task 
				Set daily_vaccinations = V_MEDIAN 
				Where country = REC.country 
					And daily_vaccinations Is Null;
					
		Exception
			When Others Then
				DBMS_OUTPUT.PUT_LINE('Loop Error : ' || REC.country || ' ' || REC.tdate || ' ' || REC.daily_vaccinations || ' ' ||SQLERRM);
		End;
	End Loop;
Exception
	When Others Then 
		DBMS_OUTPUT.PUT_LINE('General Error : ' || SQLERRM);
End;
/