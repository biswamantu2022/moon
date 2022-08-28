show databases;
use biswadb;
show tables;

select * from employee;

insert into employee values (103,'raju','11k');
insert into employee values (104,'bikash','12k');
insert into employee values (105,'jhon','10k');
insert into employee values (106,'musk','13k');
insert into employee values (107,'scot','17k');
insert into employee values (108,'russle','18k');
insert into employee values (109,'parker','15k');
insert into employee values (110,'suman','15k');

create table if not exists Departments (
dept_id varchar(255),
dept_name varchar(255),
id int(20)
);
select * from Departments;

insert into Departments values ('d01','mech',101);
insert into Departments values ('d02','ele',102);
insert into Departments values ('d03','opr',null);
insert into Departments values ('d01','mech',104);
insert into Departments values ('d02','ele',null);
insert into Departments values ('d02','ele',106);
insert into Departments values ('d02','ele',107);
insert into Departments values ('d03','opr',null);
insert into Departments values ('d03','opr',null);
insert into Departments values ('d03','opr',110);

select e.id,d.dept_id,e.name from Departments d
right join employee e
on d.id=e.id
union
select e.id,d.dept_id,e.name from Departments d
left join employee e
on d.id=e.id;

select a.name,b.name,a.salary from employee a,employee b
where a.id<>b.id and a.salary=b.salary;

select * from employee e,Departments d
where e.id=d.id;

select * from employee e
inner join Departments d
on e.id=d.id;

select d.dept_name,count(*) from employee e
inner join Departments d
on e.id=d.id
group by d.dept_name;






