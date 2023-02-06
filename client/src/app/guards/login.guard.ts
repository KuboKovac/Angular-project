import { Injectable } from '@angular/core';
import {CanActivate, Router} from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LoginGuard implements CanActivate {

  constructor(
    private router: Router
  ) {
  }

  canActivate(){
    let token = localStorage.getItem('token')

    if (token){
      return true
    }
    else{
      this.router.navigateByUrl('pageNotFound')
      return false
    }
  }

}
