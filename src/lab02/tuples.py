def format_record(rec: tuple[str, str, float]):
    fio, group, gpa = rec
    if not isinstance(fio, str) or not fio.strip():
        raise ValueError("ValueError")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("ValueError")
    if not isinstance(gpa, (int, float)):
        raise ValueError("ValueError")
    initials = ""
    parts = fio.strip().split()
    fam = parts[0]
    fam = fam.title()
    for a in parts[1:]:
        initials += a[0].upper() + "."
    if not initials:
        initials = ""
    form_gpa = f"{gpa:.2f}"
    return f"{fam} {initials}, гр. {group}, GPA {form_gpa}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
