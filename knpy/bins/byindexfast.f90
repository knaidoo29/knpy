
subroutine bin_by_index(indexes, weights, binlength, indlength, binout)

  implicit none

  integer, intent(in) :: indlength, binlength
  integer, intent(in) :: indexes(indlength)
  real, intent(in) :: weights(indlength)
  real, intent(out) :: binout(binlength)

  integer :: i
  real :: binval

  do i = 1, binlength
    binout(i) = 0.
  end do

  do i = 1, indlength
    binout(indexes(i)+1) = binout(indexes(i)+1) + weights(i)
  end do

end subroutine bin_by_index
