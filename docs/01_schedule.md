# Derivative contract schedules

Over the counter (OTC) derivative contracts are highly customisable and can have period, payment and fixing schedules depending on several parameters. These parameters define the exact payment date of the derivatives contractual payments.

```python
schedule = OTC.schedule(effective_date="10Jan2020",
                        termination_date="10Feb2030",
                        frequency="Semi-Annual"
                        business_days="Mon Tue Wed Thu Fri"
                        payment_holiday=["NY","LON"],
                        day_roll="Modified Following",
                        payment_type="In Arrears"
                        first_stub=None,
                        first_period_end_date = None,
                        last_stub="Long",
                        last_period_start_date=None
                        
                        
```


The **effective date** specifies the contractual effective date of the derivative 
The **termination date** specifies the contract termination date of the derivative 
The **frequency** specifies the occurrence of 

## holidays

Derivative contracts are signed between two parties. 
The 

## day roll
**date rolling** occurs when a payment day or date used to calculate accrued interest falls on the holiday calendar. In this case the date is moved forward or backward in time such that it falls on a business day, according with the same business calendar

The choice of the date rolling rule is conventional. Conventional rules used in finance are:
-   ```Actual``` : paid on the actual day, even if it is a non-business day.
-   ```Following``` : the payment date is rolled to the next business day.
-   ```Modified Following``` : the payment date is rolled to the next business day, unless doing so would cause the payment to be in the next calendar month, in which case the payment date is rolled to the previous business day. 
-   ```Previous```: the payment date is rolled to the previous business day.
-   ```Modified Previous```: the payment date is rolled to the previous business day, unless doing so would cause the payment to be in the previous calendar month, in which case the payment date is rolled to the next business day. Many institutions have month-end accounting procedures that necessitate this.



## stub periods

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## payment type
Specifies whether the payment occurs at the start or end of the period
If the payment occurs at the beginning of the period, specify ```In Advance"```
If the payment occurs at the end of the period, specify ```"In Arrears"```


The list of parameters to define a schedule is as follows
* [effective date](#effective-date)
* [termination date](#termination-date)
* [frequency](#payment-frequency)
* [holiday calendar](#holiday-calendar)
* [day roll](#day-roll)
* [stub periods](#stub-periods)
* [payment type](payment-type)
* [payment delay](payment-delay)
