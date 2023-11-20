DELIMITER //

CREATE TRIGGER check_email_format_trigger
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    DECLARE email_pattern VARCHAR(255);
    SET email_pattern = '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$';
    
    IF NEW.email NOT REGEXP email_pattern THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid email format.';
    END IF;
END //

DELIMITER ;