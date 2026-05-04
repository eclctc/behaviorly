<?php
    $message_sent = false;

    if (isset($_POST['email']) && $_POST['email'] != '' 
    && isset($_POST['phone']) && $_POST['phone'] != ''
    && isset($_POST['fname']) && $_POST['fname'] != ''
    && isset($_POST['lname']) && $_POST['lname'] != ''
    && isset($_POST['rbtValue']) && $_POST['rbtValue'] != ''
    && isset($_POST['notes']) && $_POST['notes'] != '')

    {
        if(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL))
        //Submit the form

        $fName = $_POST['fname'];
        $lName = $_POST['lname'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $compnay = $_POST['company'];
        $isRbt = $_POST['rbtValue'];
        $notes = $_POST['notes'];
    
        $to = 'wcoleman868@gmail.com';
        $subject = 'Behaviorly Form Submission';
        $body = "";
    
        $body .= "From: ".$fName. " ".$lName. "\r\n";
        $body .= "Email: ".$email. "\r\n";
        $body .= "Phone Number: ".$phone. "\r\n";
        $body .= "Company: ".$company. "\r\n";
        $body .= "Is an RBT: ".$isRbt. "\r\n";
        $body .= "Additional Notes: ".$notes. "\r\n";
    
        //mail($to, $subject, $body);

        $message_sent = true;
        echo "message_sent";
    }
    else
    {
        echo "We messed up";
    }
?>