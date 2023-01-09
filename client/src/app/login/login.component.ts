import { Component, OnInit } from '@angular/core';
import {AuthService} from "../services/auth.service";
import {MatDialog} from "@angular/material/dialog";
import {Router} from "@angular/router";
import {Login} from "../../Models/login";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  constructor(
    private authService: AuthService,
    private dialog: MatDialog,
    private router: Router
  ) { }

  login: Login = new Login('','');
  ngOnInit(): void {

  }
  public onSubmit(){
    this.authService.login(this.login).subscribe(
      response => {
        console.log(response)
      }
    )
    this.dialog.closeAll()
    this.router.navigateByUrl('home')
  }
}
