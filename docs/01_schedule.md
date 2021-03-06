# Swap schedules

Swaps are over the counter (OTC) derivative contracts and are highly customisable with period, payment and fixing schedules depending on several parameters. These parameters can define the exact dates of the derivatives contractual payments, or for calculating the accrued interest amounts. 

Below is a call to the ```OTC.schedule()``` function.
We will run through each of the function parameters, explain their meaning and acceptable input values.

```python
schedule = OTC.schedule(start_date="10Jan2020",
                        end_date="10Feb2030",
                        frequency="Semi-Annual"
                        business_days="Mon Tue Wed Thu Fri"
                        payment_holiday=["NY","LON"],
                        day_roll_convention="Modified Following",
                        day_roll=10
                        payment_type="In Arrears",
                        payment_delay=1
                        first_stub=None,
                        first_period_end_date=None,
                        last_stub="Long",
                        last_period_start_date=None)              
```
---

The ```start_date``` specifies the contractual effective date of the swap 

---

The  ```end_date``` specifies the contractual termination date of the swap. 

---

The ```frequency``` specifies the occurrence of period. Valid values include:
* ```"Weekly"```
* ```"Monthly"```
* ```"Quarterly"```
* ```"Semi-Annual"```
* ```"Annual"```
* ```"Zerocoupon"```

A ```"Zerocoupon"``` leg of a swap has only a single payment at maturity (no interim payments). 

---

The ```business_days``` parameter sets the business days of the week.
The majority of countries observe the Monday-Friday as business days, with Saturday-Sunday as the weekend. Hence for the majority of the time use ```business_days="Mon Tue Wed Thu Fri"```.

Israel and Muslim countries and  observe Sunday–Thursday as business days, with Friday-Saturday as the weekend. 
To observe these business days set ```business_days="Sun Mon Tue Wed Thu"```. 

---

Date rolling occurs when a payment day or date used to calculate accrued interest falls on a non-business day or holiday. In this case the date is moved forward or backward in time such that it falls on a business day, according with the same business calendar.

Day roll conventions available include:
-   ```Actual``` : paid on the actual day, even if it is a non-business day.
-   ```Following``` : the payment date is rolled to the next business day.
-   ```Modified Following``` : the payment date is rolled to the next business day, unless doing so would cause the payment to be in the next calendar month, in which case the payment date is rolled to the previous business day. 
-   ```Previous```: the payment date is rolled to the previous business day.
-   ```Modified Previous```: the payment date is rolled to the previous business day, unless doing so would cause the payment to be in the previous calendar month, in which case the payment date is rolled to the next business day. Many institutions have month-end accounting procedures that necessitate this.

---

```day_roll``` specifies the payment day of month. Valid values include ```1,2,3,...,29,30,31,"EndOfMonth"```. 

```day_roll="EndOfMonth"``` specifies that payment date is to occur on the last day of the month.

---

```payment_type``` specifies whether the payment occurs at the start or end of the period

If the payment occurs at the beginning of the period, specify ```payment_type="In Advance"```

If the payment occurs at the end of the period, specify ```payment_type="In Arrears"```

---

```payment_offset``` specifies the business day offset from the period end (or the period start), if ```payment_type="In Arrears"```, (if ```payment_type="In Advance"```) before the payment is made. 

```payment_offset``` can take any integer value (both positive and negative values). A positive value for ```payment_offset``` indicates a later payment (a delay), while a negative number indicates an earlier payment. 

---

Stubs occur when the contractual coupon periods of the swap do not divide exactly into into the swaps lifespan.

For example, for a swap effective from 10-Jan-2020, and terminating on 10-Feb-2020, with a semi-annual frequency, the lifespan is 10 years and one month which is not exactly divisable by the semi-annual frequency. This results in a non-regular period known as a **stub period**.

If a swap has a stub, we should define where the stub period falls. The stub period can occur in the first or last period of the swap and can be longer or shorter than a regular period. 

### first_stub

### first_period_end_date

### last_stub

### last_period_start_date


For example, for a swap effective from 10-Jan-2020, and terminating on 10-Feb-2020, with a semi-annual frequency, the stub could be either 1-month or 7-months long and could be the first or the last period of the swap. 

If the stub period is 

